var sidenav = document.querySelector('#sidenav')
var main = document.querySelector('#main')

sidenav.addEventListener('mouseleave', function(){
    if (this.classList.contains('open')){
        this.classList.remove('open')
        this.classList.add('close')
        sidenav.classList.remove('w-44')
        changeSideNavBtns(false)
    } 
})

sidenav.addEventListener('mouseover', function(){
    if (this.classList.contains('close')) {
        this.classList.add('open')
        this.classList.remove('close')
        
        sidenav.classList.add('w-44')
        changeSideNavBtns(true)
    }
})

function changeSideNavBtns(status){
    var sidenavMenu = document.querySelectorAll('.sidenav_menu')
    for (let menu of sidenavMenu) {
        for (let btn of menu.children) {
            btn = btn.firstChild
            let text
            if (status) {
                btn.parentElement.classList.add('w-24')
                text = btn.getAttribute('data-open')
            } else {
                btn.parentElement.classList.remove('w-24')
                text = btn.getAttribute('data-close')
            }
            btn.textContent = text
        }
    }
}