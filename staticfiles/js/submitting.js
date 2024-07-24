try {    
    let loader = document.querySelector('.central-loader-cont')
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



    function onBackButtonEvent(event) {
        // Prevent the default action
        loader.classList.remove('loader-cont')
        console.log("Back button was pressed!");
        // You can add any other logic you need here
    }

    // Listen for the popstate event
    window.addEventListener('popstate', onBackButtonEvent);

    // Add a history entry to ensure the back button can be pressed
    history.pushState(null, null, location.href);

    // Optional: Handle page refresh or close
    window.addEventListener('beforeunload', (event) => {
        // loader.classList.remove('loader-cont') 
        console.log("Page is being closed or refreshed!");
    });
}catch (error) {
    console.log(error)
}