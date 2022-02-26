import "CoreLibs/graphics"
import "CoreLibs/object"

gfx = playdate.graphics
snd = playdate.sound

local effect = snd.overdrive.new()
effect:setMix(0)
snd.addEffect(effect)

instruments = {}

function removeNotes(data)
	for note, instrument in pairs(instruments) do
		if not data[note] then
			instruments[note]:setVolume(0)
			instruments[note]:allNotesOff()
			instruments[note] = nil
		end
	end
end

function addNotes(data)
	for note, volume in pairs(data) do
		if not instruments[note] then
			local synth = snd.synth.new(playdate.sound.kWavePOVosim)
			synth:setADSR(0, 0, 1, 2)
			local instrument = snd.instrument.new(synth)
			instruments[note] = instrument
			instrument:setVolume(volume / 100)
			instrument:playMIDINote(note, 1, 1)
		end
	end
end

function drawNotes()
	gfx.clear()
	i = 0
	for y = 0, 8 do
		for x = 0, 15 do
			if instruments[tostring(i)] then
				gfx.fillCircleAtPoint(x * 20 + 50, y * 20 + 40, 8)
			else
				gfx.drawCircleAtPoint(x * 20 + 50, y * 20 + 40, 8)
			end
			i += 1
		end
	end
end

function playdate.update()
	local data = playdate.datastore.read('midi') or {}

	removeNotes(data)
	addNotes(data)
	drawNotes()
end
