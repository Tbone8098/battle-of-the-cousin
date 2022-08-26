var btnAddKiddo = document.querySelector('.btn-add-kiddo')
var sectionAddKiddo = document.querySelector('.section-add-kiddo')

btnAddKiddo.addEventListener('click', function(){
    if (sectionAddKiddo.classList.contains('hidden')){
        sectionAddKiddo.classList.remove('hidden')
        sectionAddKiddo.parentElement.classList.remove('scale-y-0')
    } else {
        sectionAddKiddo.classList.add('hidden')
        sectionAddKiddo.parentElement.classList.add('scale-y-0')
    }
})