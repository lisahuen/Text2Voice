import edge_tts
import asyncio

TEXT = ""
text_file = 'C:\\tmp\\text2voice.txt'
with open(text_file, 'rb') as f:
    data = f.read()
    TEXT = data.decode('utf-8')

voice = 'af-ZA-AdriNeural'
voice_file = 'C:\\tmp\\output\\text2voice.mp3'
rate = '-4%'
volume = '+0%'

async def GenerateSoundTrack():
    tts = edge_tts.Communicate(text=TEXT, voice=voice, rate=rate, volume=volume)
    await tts.save(voice_file)


asyncio.run(GenerateSoundTrack())