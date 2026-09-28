let items=document.getElementById('items')
let s=''
fetch("http://127.0.0.1:8000/products").then(r => r.json()).then (res =>{
    console.log(res)
    let data=res.prodcuts
    let n=data.length
    for(let i=0;i<n;i++){
        console.log(data[i])
        s+='<div class="card">'+
                '<img class="picture" src='+data[i].image +'/>'+
                '<div class="name">'+data[i].name+'</div>'+
                '<div class="price">₹ '+data[i].price+'.00</div>'+
            '</div>'
    }
        items.innerHTML=s
})



