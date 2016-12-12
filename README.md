# Word of the Day
An Alexa Flash Briefing skill to learn you a new, interesting word everyday. Powered by the Wordnik API.

# Design
A scheduled lambda pulls down the new word each day, formats it into the Alexa Flash Briefing json format and places it into an S3 bucket configured as as static website fronted by CloudFront.  The Alexa service pulls the file whenever someone uses the skill from the S3 website/CloudFront.

# Usage
Instructions on how to enable and use the skill with Alexa-enabled devices is at https://byu-oit-appdev.github.io/word-of-the-day-alexa-flash-briefing-skill/

Requirements:
* python2.7
* jq
* sed

Alexa Skill Icon Image Credit: https://commons.wikimedia.org/wiki/File:Accessories-dictionary.svg
