# Reflection

## What Worked Well
The agent was able to take a customer message and retrieve HVAC information, then suggesting next steps. Setting up tools like basic scheduling logic and simulated customer support responses made the agent feel more realistic and aligned with real HVAC business needs.

## What Didn’t Work
One issue I ran into was that the agent would sometimes misunderstand customer inputs or give overly generic answers. I adjusted the prompts and added clearer instructions. Another one was It wouldn't let me put in my api keys. 

## Biggest Challenge
The biggest challenge was getting the agent to run correctly in Colab with the proper file structure and imports. Errors like “file not found” or module import issues slowed down progress. I solved this by carefully checking the directory structure and adding new lines of code.

## Path Decision
The path I decided with was Single Agent. This worked well because it kept the system simpler and easier to manage.

## What I Would Build Next
I would expand this into a more advanced system. I would add image recognition using a CNN, so customers could upload pictures of HVAC issues and the agent could analyze them. Maybe add more API's and possibly using multi agent system