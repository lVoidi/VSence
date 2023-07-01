# VSence - Custom DRC 
This is the custom Discord Rich Presence i personally use. In this repo, i will teach you 
how you can create your own Rich Presence with pypresence module. This program works only 
on Windows for personal reasons, but if you're a Linux user i'm pretty sure you're used to 
this. By the way, just follow the steps on the following guide to get it working!

## Installation
We need to install psutil and pypresence in order to make this work. 
```bash 
pip install pypresence psutil 
``` 
Obviously you need discord installed. You can **setup this program to run on 
startup** because it will automatically start only until discord is opened. 
This step depends on your current environment and it's totally optional. 

## How to create a custom DRC very easly
I will explain how to get and ending result like this.
![result](https://imgur.com/i3I4UfK.png)
The phrases are in spanish but that doesn't matter here. I will show you how to replicate this. 

First of all, you need to create a client for your RPC. In order to do that, go to [this link](https://discord.com/developers/applications). Then, create a new application and name it however you want. The name of this application will be the title of 
your Rich Presence, so choose wisely. Get your client id in the OAuth2 section. 
![OAuth2](https://imgur.com/yDtl31m.png). 


Now we get to the code! 
### Coding part
Initialize your presence object 
```py 
import pypresence
import os 

pid = os.getpid() # We will need this later
presence = pypresence.Presence(client_id="your client id")
presence.connect()
```
We need to constantly update our Rich Presence, so we start a while loop. Inside it, 
we update our Rich Presence with the information you want. Check [pypresence docs](https://qwertyquerty.github.io/pypresence/html/doc/presence.html)
```py 
 while True:
        try:
            # IMPORTANT
            # Check pypresence documentation to fill this data
            presence.update(
                pid=pid, # This is why we needed that line of code before
                state="Your status", 
                details="Any detail", 
                large_image="https://images.com/any_image_link.png",
            )
        # This is necessary in case you need to close it
        except KeyboardInterrupt:
            print("Closing program...")
            presence.close()
            presence.clear(os.getpid())
```

## Run
Now run the program and you're done!