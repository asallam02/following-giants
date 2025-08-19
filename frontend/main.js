// Initialize map
const map = L.map('map').setView([0, 0], 2); // Center on ocean, zoomed out

// Add OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: 'Map data © OpenStreetMap contributors'
}).addTo(map);

// Fetch whale data from backend
fetch('http://127.0.0.1:8000/api/whales/blue?limit=500')
  .then(response => response.json())
  .then(data => {
    data.forEach(record => {
      if (record.latitude && record.longitude) {
        L.circleMarker([record.latitude, record.longitude], {
          radius: 5,
          color: 'blue',
          fillOpacity: 0.6
        }).bindPopup(`
          <b>${record.commonName}</b><br/>
          Scientific: ${record.scientificName}<br/>
          Date: ${record.eventDate}<br/>
          Platform: ${record.platform || 'N/A'}<br/>
          Count: ${record.individualCount || 'N/A'}
        `).addTo(map);
      }
    });
  })
  .catch(err => console.error('Error fetching whale data:', err));
