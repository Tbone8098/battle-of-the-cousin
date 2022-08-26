var links = document.querySelectorAll('.link')

for (let link of links) {
    link.addEventListener('click', function(){
        hideAll()
        let page = link.getAttribute('link-to')
        page = document.querySelector(`#${page}`)
        showPage(page)
        link.classList.add('underline')
    })
}

function hideAll(){
    let allSubpages = document.querySelectorAll('.subpage')
    for (let page of allSubpages) {
        page.classList.add('hidden')
    }
    for (let link of links) {
        link.classList.remove('underline')
    }
}

function showPage(page){
    page.classList.remove('hidden')
}