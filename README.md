# word-of-the-day-alexa-flash-briefing-skill
An Alexa Flash Briefing skill for telling the word of the day.  Powered by the Wordnik API.

# Design
A scheduled lambda pulls down the new word each day, formats it into the Alexa Flash Briefing json format and places it into an S3 bucket configured as as static website fronted by CloudFront.  The Alexa service pulls the file whenever someone uses the skill from the S3 website/CloudFront.

Requirements:
* python2.7
* jq
* sed
