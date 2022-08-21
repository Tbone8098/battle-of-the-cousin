let loginForm = document.querySelector('#login-form')
let registerForm = document.querySelector('#register-form')

// frontend validation for the forms
// registerForm
for (const el of registerForm.children) {
    checkInputs(el)
}
for (const el of loginForm.children) {
    checkInputs(el)
}

// check inputs
function checkInputs(el){
    let input = findInput(el)
    if (input){
        let reqLen = input.getAttribute('req_len')
        console.log(input, reqLen);
        setEventListener(input, reqLen)
    }
}

function setEventListener(inputEl, req) {
    inputEl.addEventListener('keyup', function(){
        let siblings = inputEl.parentElement.children
        for (let child of siblings) {
            if (child.classList.contains('errDiv')) {
                var span = child.lastElementChild
            }
        }
        if (inputEl.value.length === 0 || inputEl.value.length > parseInt(req)){
            span.textContent = ''
        } else if (inputEl.value.length < parseInt(req)){
            span.textContent = `Field must be ${req} characters`
        } 
    })
}

function findInput(el) {
    if (el.children.length <= 0) {
        return false
    } else {
        for (let child of el.children) {
            if (child.classList.contains('input')) {
                return child
            } else {
                return findInput(child)
            }
        }
    }
}

// Turning on the family code
var familyBtn = document.querySelector('#join_family')
var familyCodeEl = document.querySelector('#family_code')
var familyNameEl = document.querySelector('#family_name')
familyBtn.addEventListener('click', function () {
    if (this.checked) {
        switchCodeAndName(true)
    } else {
        switchCodeAndName(false)
    }
})

function switchCodeAndName(codeShowing) {
    if (codeShowing) {
        familyCodeEl.classList.remove('scale-x-0')
        familyNameEl.classList.add('scale-x-0')
    } else {
        familyCodeEl.classList.add('scale-x-0')
        familyNameEl.classList.remove('scale-x-0')
    }
}


// Switching between login and register
var loginRegBtn = document.querySelector('#loginReg-btn')
loginRegBtn.addEventListener('click', function () {
    if (this.textContent === 'Go To Register') {
        this.textContent = 'Go To Login'
        this.classList.remove('bg-slate-500')
        this.classList.add('bg-blue-500')

        loginForm.classList.add('translate-x-[-250%]')
        registerForm.classList.remove('translate-x-[-250%]')
    } else {
        this.classList.add('bg-slate-500')
        this.classList.remove('bg-blue-500')
        this.textContent = 'Go To Register'

        loginForm.classList.remove('translate-x-[-250%]')
        registerForm.classList.add('translate-x-[-250%]')
    }
})


// Switching between Child and Parent mode on the forms
var userType = document.querySelectorAll('.user_type')
var joiningFamilyCheckbox = document.querySelector('#joining-family-checkbox')
var regUsername = document.querySelector('#reg-username')
var parentForm = document.querySelector('#parent-form')
var kidForm = document.querySelector('#kid-form')

for (let btn of userType) {
    btn.addEventListener('change', function () {
        let regEmail = document.querySelector('.reg-email')
        if (this.value === 'child') {
            regEmail.style.display = 'none'
            joiningFamilyCheckbox.style.display = 'none'
            joiningFamilyCheckbox.children[0].checked = false
            familyNameEl.style.display = 'none'
            switchCodeAndName(true)
            familyCodeEl.classList.add('w-full')
            parentForm.classList.add('hidden')
            kidForm.classList.remove('hidden')
        } else {
            regEmail.style.display = 'flex'
            joiningFamilyCheckbox.style.display = 'flex'
            familyNameEl.style.display = 'flex'
            switchCodeAndName(false)
            familyCodeEl.classList.remove('w-full')
            parentForm.classList.remove('hidden')
            kidForm.classList.add('hidden')
        }
    })
}