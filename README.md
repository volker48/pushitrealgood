#Push it real good

I've been running a ton of machine learning experiments lately and I wanted something to notify me when my jobs done so
I don't have to check my jupyter notebook constantly (or listen for my fans to stop spinning like my laptop is about to execute a vertical take off).


###Usage
Before running your application you'll need to set some environment variables.

1. `PIRG_TOKEN` your API token from pushover
2. `PIRG_USER` the user key from pushover

Then,

```
from pirg import Pirg

with Pirg('work complete'):
    #some long running task happens here
```

After the long running task completes you'll receive a push notification that says `work complete`.

###Alternative usage

If you don't want to set environment variables you can pass the token and user key directly into the Pirg constructor: `Pirg('work complete', token='abc123', user='abc123')`