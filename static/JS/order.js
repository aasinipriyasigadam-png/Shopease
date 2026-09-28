function ordered_items(product_id){
    console.log(product_id)
     fetch("/orders/"+product_id+"/", {
        method: "post"
     }).then(res => res.json()).then(r => {
      console.log(r)
        window.location.href='/orders'
     })
}

