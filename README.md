#  Simple request maker 
## Examples
```bash
srm -u https://api.ipify.org # Get request.
``` 

```bash
srm -u https://httpbin.org/post -d "Some Example Data" # Post request.  (Data)
``` 

```bash
srm -u https://httpbin.org/post -j '{"Some Example Data": "hey"}' # Post request. (Json)
``` 