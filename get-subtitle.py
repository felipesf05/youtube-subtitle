from youtube_transcript_api import YouTubeTranscriptApi
import json
# assigining srt variable with the list of dictonaries 
# obtained by the the .get_transcript() function
# and this time it gets only teh subtitles that 
# are of english langauge.
# retrieve the available transcripts
transcript_list = YouTubeTranscriptApi.list_transcripts('xC-c7E5PK0Y')
#srt = YouTubeTranscriptApi.get_transcript("DqTITcMq68k", 
#                                          languages=['pt'])
  
# prints the result
#print(srt)

# object
for transcript in transcript_list:
	legenda = transcript.translate('pt').fetch()

#for i in legenda:
#	print(i["text"])	
	#legenda_json = json.loads(i)
	#print(legenda_json["Text"])


#for l in legenda:
#	print(l.text)
with open("legenda.txt", "w") as f:
    # iterating through each element of list srt
  	for i in legenda:
	    f.write(str(i["text"])+"\n")