function add_to_cart(product_id){
    console.log(product_id)
     fetch("/cart/"+product_id+"/", {
        method: "post"
     }).then(res => res.json())
     .then(r => {
        console.log(r)
     })
}
