import asyncio
import aiohttp
import aiortc
from aiohttp import web

async def offer(request):
    # Create a peer connection for the caller
    pc = aiortc.RTCPeerConnection()
    # Add media tracks for audio and video
    await pc.addTrack(await aiortc.getUserMedia())
    # Create an offer and send it to the callee
    offer = await pc.createOffer()
    await pc.setLocalDescription(offer)
    return web.json_response({"sdp": offer.sdp})

async def answer(request):
    # Create a peer connection for the callee
    pc = aiortc.RTCPeerConnection()
    # Receive the offer from the caller
    offer = aiortc.RTCSessionDescription(sdp=request.query['sdp'])
    await pc.setRemoteDescription(offer)
    # Add media tracks for audio and video
    await pc.addTrack(await aiortc.getUserMedia())
    # Create an answer and send it back to the caller
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)
    return web.json_response({"sdp": answer.sdp})

async def hi(req):
    return web.Response(body="hi")

app = web.Application()
app.add_routes([web.get('/offer', offer), web.get('/answer', answer),web.get('/', hi)])

if __name__ == '__main__':
    web.run_app(app)
