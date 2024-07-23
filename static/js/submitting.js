const loader = document.querySelector('.central-loader-cont')
const forms = document.querySelectorAll('form')
const hyperLinks = document.querySelectorAll("a")
const buttons = document.querySelectorAll('button')
loader.classList.remove('loader-cont')
forms.forEach((element)=>{
    element.addEventListener('submit', function(e){
        loader.classList.add('loader-cont')
        buttons.forEach(element => {
            element.style.opacity='0.7'
            element.setAttribute('disabled', true)
            element.textContent="Submitting..."
        });
    
    })

})

hyperLinks.forEach((element)=>{
    element.addEventListener('click', function(e){
        console.log('submiting')
        loader.classList.add('loader-cont')
    })

})



