    const optionAWrapper=document.querySelector('.a_wrapper')
    const optionBWrapper=document.querySelector('.b_wrapper')
    const optionCWrapper=document.querySelector('.c_wrapper')
    const optionDWrapper=document.querySelector('.d_wrapper')
    const instruct = document.querySelector('.instruct')
    const addOptionsBtn=document.querySelector('.add-option-btn')
    const chooseCorrectBtn=document.querySelector('.choose-correct-btn')
    const question = document.querySelector('.question-textarea')
    const optionA= optionAWrapper.querySelector('textarea')
    const optionB= optionBWrapper.querySelector('textarea')
    const optionC= optionCWrapper.querySelector('textarea')
    const optionD= optionDWrapper.querySelector('textarea')



    let state=0

    
    const appendError= (message,non_fatal)=>{    
        instruct.textContent=message
        instruct.classList.add('wrong-answer')
        instruct.style.display='block'
        instruct.style.border='transparent'
        if(!non_fatal){
            instruct.style.color='red'
        }
    }

    
    //Clear error after new input
    const inputs = document.querySelectorAll('input, textarea, select');
    inputs.forEach(input => {
        input.addEventListener('input', handleInputChange);
    });
    function handleInputChange(event) {
        instruct.textContent=''
        instruct.style.display='none'
        instruct.style.color='black'
    }


    addOptionsBtn.addEventListener('click',()=>{
        // optionAWrapper.classList.add('active');
        if(chooseCorrectBtn.textContent=="Submit"){
            appendError('Go ahead and choose the correct answer',true)
            return
        }
        if(!question.value){   
            appendError('Question cannot be empty')
            return 
        }
        state++
        switch (state) {
            case 1:
                optionAWrapper.classList.add('active');
                optionAWrapper.style.transform = "translateY(0px)"
                optionA.focus()
                break;
            case 2:
                optionAWrapper.style.transform = "translateY(80px)"
                optionBWrapper.style.transform = "translateY(-120px)"
                optionBWrapper.classList.add('activeb');
                optionB.focus()
                break;
            case 3:
                optionAWrapper.style.transform = "translateY(180px)"
                optionBWrapper.style.transform = "translateY(-20px)"
                optionCWrapper.style.transform = "translateY(-220px)"
                optionCWrapper.classList.add('activec');
                optionC.focus()
                break;
            case 4:
                optionAWrapper.style.transform = "translateY(320px)"
                optionBWrapper.style.transform = "translateY(120px)"
                optionCWrapper.style.transform = "translateY(-80px)"
                optionDWrapper.style.transform = "translateY(-300px)"
                optionDWrapper.classList.add('actived');
                optionD.focus()
                break;
            default:
        }
    })

    chooseCorrectBtn.addEventListener('click',(e)=>{
        if(chooseCorrectBtn.textContent=='Next'){
            e.preventDefault()
        }
        if(!document.querySelector('#answer').value && chooseCorrectBtn.textContent=='Submit'){
            e.preventDefault()
            appendError("Choose an answer")
            return
        }
        if(!optionAWrapper.children[1].value||!optionBWrapper.children[1].value){
            appendError('Fill in at least two options')
            return 
        }

        instruct.textContent='Choose the best answer'
        instruct.style.display='block'
        instruct.style.color='black'
        chooseCorrectBtn.textContent='Submit'
        document.querySelectorAll('textarea').
            forEach((option)=>{
                option.style.opacity="0.7"
                option.style.cursor='pointer'
                option.addEventListener('focus',()=>{
                    if(!option.value){
                        appendError("Nah, You can't really choose an empty answer")
                        option.style.border='3px solid red'
                        return    
                    }
                    option.style.border='3px solid green'
                    document.querySelector('#answer')
                    .value=option.value
                })
                option.addEventListener('blur',()=>{
                    option.style.border='1px solid gray'
                })
                addOptionsBtn.setAttribute('disabled',true)
                option.setAttribute('readonly',true)
                
            })
    })        
