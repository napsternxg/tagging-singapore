var t=document.getElementById("directory");
var r=document.createElement("tr");
var c=document.createElement("td");
c.appendChild(document.createTextNode("{{location.locationName}}"));
r.appendChild(c)
c=document.createElement("td");
c.appendChild(document.createTextNode("{{location.locationLatitude}}"));
r.appendChild(c)
c=document.createElement("td");
c.appendChild(document.createTextNode("{{location.locationLongitude}}"));
r.appendChild(c)
c=document.createElement("td");
c.appendChild(document.createTextNode("{{location.locationName}}"));
r.appendChild(c)
c=document.createElement("td");
c.appendChild(document.createTextNode("{{location.locationName}}"));
r.appendChild(c)
t.appendChild(r);