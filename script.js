document.addEventListener('DOMContentLoaded',()=>{
  const btn=document.querySelector('.menu-toggle');
  const nav=document.getElementById('nav');
  if(btn&&nav){
    const close=()=>{nav.classList.remove('open');btn.setAttribute('aria-expanded','false');};
    btn.addEventListener('click',()=>{
      const open=nav.classList.toggle('open');
      btn.setAttribute('aria-expanded',String(open));
    });
    nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',close));
    document.addEventListener('keydown',e=>{
      if(e.key==='Escape'&&nav.classList.contains('open')){close();btn.focus();}
    });
    document.addEventListener('pointerdown',e=>{
      if(nav.classList.contains('open')&&!nav.contains(e.target)&&!btn.contains(e.target))close();
    });
    const mq=window.matchMedia('(min-width: 671px)');
    mq.addEventListener?.('change',e=>{if(e.matches)close();});
  }
  const year=document.getElementById('year');
  if(year)year.textContent=String(new Date().getFullYear());
  const print=document.getElementById('print');
  if(print)print.addEventListener('click',()=>window.print());
});