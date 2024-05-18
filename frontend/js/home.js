// main.js
import { products } from '../data/products.js';

const productsContainer = document.getElementById('products-container');

products.map(product => {
    // Create the product div
    const productDiv = document.createElement('div');
    productDiv.classList.add('products');

    // Create and populate the image div
    const productImageDiv = document.createElement('div');
    productImageDiv.classList.add('product-image');
    const productImage = document.createElement('img');
    productImage.src = product.image;
    productImage.alt = product.name;
    productImageDiv.appendChild(productImage);

    // Create and populate the name div
    const productNameDiv = document.createElement('div');
    productNameDiv.classList.add('product-name');
    const productName = document.createElement('p');
    productName.textContent = product.name;
    productNameDiv.appendChild(productName);

    // Create and populate the price div
    const productPriceDiv = document.createElement('div');
    productPriceDiv.classList.add('product-price');
    productPriceDiv.textContent = `$${product.price}`;

    // Create and populate the rating div
    const productRatingDiv = document.createElement('div');
    productRatingDiv.classList.add('product-rating');
    
    // logic to display rating icons
    for (let i = 0; i < product.rating; i++) {
        const ratingIcon = document.createElement('div');
        ratingIcon.textContent = '★'; 
        productRatingDiv.appendChild(ratingIcon);
    }
    for (let i = product.rating; i < 5; i++) {
        const emptyIcon = document.createElement('div');
        emptyIcon.textContent = '☆'; 
        productRatingDiv.appendChild(emptyIcon);
    }

    // Append all the parts to the product div
    productDiv.appendChild(productImageDiv);
    productDiv.appendChild(productNameDiv);
    productDiv.appendChild(productPriceDiv);
    productDiv.appendChild(productRatingDiv);

    // Append the product div to the products container
    productsContainer.appendChild(productDiv);
});
