var modalBtn = document.querySelectorAll('.modal-btn')

for (let btn of modalBtn) {
    btn.addEventListener('click', function(){
        modalWrapperName = btn.getAttribute('modal_name')
        modalWrapper = document.querySelector(`#${modalWrapperName}`)
        modalWrapper.classList.remove('hidden') 
    })
}

var modalWrappers = document.querySelectorAll('.modal_wrapper')
for (let wrapper of modalWrappers) {
    wrapper.addEventListener('click', function(event){
        closeModal(wrapper)
    })
}

var modalContainers = document.querySelectorAll('.modal_container')
for (let container of modalContainers) {
    container.addEventListener('click', function(event){
        event.stopPropagation()
    })
}

var modalCloseBtn = document.querySelectorAll('.close-btn')

for (let btn of modalCloseBtn) {
    btn.addEventListener('click', async function(){
        let wrapper = findWrapper(btn)
        closeModal(wrapper)
    })
}

function closeModal(wrapper){
    wrapper.classList.add('hidden')
}

function findWrapper(item){
    var parent = item.parentElement
    if ( parent.classList.contains('modal_wrapper')){
        return parent
    } else {
        return findWrapper(parent)
    }
}