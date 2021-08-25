
const inputBox = document.querySelector('#address');
const button = document.querySelector('.searchAddress');
const submit = document.querySelector('.submitButton')
const map = document.querySelector('iframe')
const card = document.querySelector('.card-text')
const latitude = document.querySelector('.lat')
const longitude = document.querySelector('.lng')
async function getAddress(address) {
	try{
		
		const url = `https://maps.googleapis.com/maps/api/geocode/json?address=${address.replace(/\s/g, '+')}&key=`+API_KEY;
        const res = await axios.get(url);
        console.log(res.data);
        const lat = res.data.results[0].geometry.location.lat;
        const lng = res.data.results[0].geometry.location.lng;
        if((lat >= 17.1 && lat <= 17.7) && (lng >= 78.1 && lng <= 78.8)){
        latitude.value = lat;
        longitude.value = lng;
        map.src = `https://www.google.com/maps/embed/v1/place?key=`+ API_KEY +`&q=${address.replace(/\s/g, '+')}`;
        card.innerText = `Address: ${res.data.results[0].formatted_address}`
        }else{
            card.innerText = `Address: ${res.data.results[0].formatted_address} is not within Hyderabad City limits, please choose another address`
        }
        
	}catch(error){
        console.error(error);
        const inputBox = document.querySelector('#address');
        inputBox.value = 'Unable to find address'
}
}


button.addEventListener('click',()=>{
    if (inputBox.value){const text = inputBox.value;
        getAddress(text);
}})

window.addEventListener('load',()=>{
    if (inputBox.value!='' && inputBox.value!= " "){const text = inputBox.value;
       getAddress(text);
}})




