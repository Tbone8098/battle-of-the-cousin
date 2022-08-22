var joinFamilyCheckbox = document.querySelector('#join_family_checkbox')
var familyCode = document.querySelector('#family_code_div')
var familyName = document.querySelector('#family_name_div')

joinFamilyCheckbox.addEventListener('change', function(){
    if (joinFamilyCheckbox.checked === true){
        familyCode.classList.remove('scale-x-0', '-z-10')
        familyName.classList.add('scale-x-0', '-z-10')
    } else {
        familyCode.classList.add('scale-x-0', '-z-10')
        familyName.classList.remove('scale-x-0', '-z-10')
    }
})