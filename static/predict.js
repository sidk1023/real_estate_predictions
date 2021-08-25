const map = document.querySelector('iframe')
const card = document.querySelector('.card-text')
const addressBox = document.querySelector('.address')
async function getAddress(address) {
	try{
		
		const url = `https://maps.googleapis.com/maps/api/geocode/json?address=${address.replace(/\s/g, '+')}&key=`+ API_KEY;
        const res = await axios.get(url);
        console.log(res.data);
        map.src = `https://www.google.com/maps/embed/v1/place?key=` + API_KEY + `&q=${address.replace(/\s/g, '+')}`;
        addressBox.innerText = `${res.data.results[0].formatted_address}`
       
	}catch(error){
        console.error(error);
        addressBox.value = 'Unable to fetch address'
}
}


//window.addEventListener('load',()=>{if (addressBox.innerText){const text = addressBox.innerText; getAddress(text);}})

document.addEventListener("DOMContentLoaded", function() {
  const text = addressBox.innerText; 
  getAddress(text);
});