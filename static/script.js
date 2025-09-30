let cart = JSON.parse(localStorage.getItem("cart")) || [];

// Fetch products from backend
fetch("/products")
  .then(res => res.json())
  .then(products => {
    const productList = document.getElementById("product-list");
    products.forEach(p => {
      const div = document.createElement("div");
      div.className = "product";
      div.innerHTML = `
        <img src="${p.imageUrl}" alt="${p.name}">
        <h3>${p.name}</h3>
        <p>₹${p.price}</p>
        <button onclick="addToCart(${p.id}, '${p.name}', ${p.price})">Add to Cart</button>
      `;
      productList.appendChild(div);
    });
  });

function addToCart(id, name, price) {
  let item = cart.find(p => p.id === id);
  if (item) {
    item.quantity += 1;
  } else {
    cart.push({ id, name, price, quantity: 1 });
  }
  saveCart();
  renderCart();
}

function renderCart() {
  const cartItems = document.getElementById("cart-items");
  cartItems.innerHTML = "";
  let total = 0;

  cart.forEach(item => {
    total += item.price * item.quantity;
    let li = document.createElement("li");
    li.innerHTML = `
      ${item.name} (x${item.quantity}) - ₹${item.price * item.quantity}
      <button onclick="changeQuantity(${item.id}, 1)">+</button>
      <button onclick="changeQuantity(${item.id}, -1)">-</button>
    `;
    cartItems.appendChild(li);
  });

  document.getElementById("total").innerText = `Total: ₹${total}`;
}

function changeQuantity(id, delta) {
  let item = cart.find(p => p.id === id);
  if (item) {
    item.quantity += delta;
    if (item.quantity <= 0) cart = cart.filter(p => p.id !== id);
  }
  saveCart();
  renderCart();
}

function saveCart() {
  localStorage.setItem("cart", JSON.stringify(cart));
}

document.getElementById("checkout").addEventListener("click", () => {
  fetch("/checkout", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ items: cart })
  })
    .then(res => res.json())
    .then(data => {
      alert(data.message);
      cart = [];
      saveCart();
      renderCart();
    });
});

renderCart();
 