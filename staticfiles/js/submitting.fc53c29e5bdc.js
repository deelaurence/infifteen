const nav = document.querySelector('nav')
const loader = document.querySelector('.central-loader-cont')
const forms = document.querySelectorAll('form')
const buttons = document.querySelectorAll('button')
loader.classList.remove('loader-cont')
forms.forEach((element)=>{
    element.addEventListener('submit', function(e){
        console.log('submiting')
        loader.classList.add('loader-cont')
        buttons.forEach(element => {
            element.style.opacity='0.5'
            element.setAttribute('disabled', true)
            element.textContent="Submitting..."
        });
    
    })

})



console.log(nav)



