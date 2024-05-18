// main.js
import { popularProducts, featuredProducts } from '../data/products.js';

const featuredProductsContainer = document.getElementById('featured-products-container');
const popularProductsContainer = document.getElementById('popular-products-container');


popularProducts.map(product => {
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
    const productName = document.createElement('h4');
    productName.textContent = product.name;
    productNameDiv.appendChild(productName);

    // Create and populate the price div
    const productPriceDiv = document.createElement('div');
    productPriceDiv.classList.add('product-price');
    productPriceDiv.textContent = `Price:  $${product.price}`;

    // Create and populate the rating div
    const productRatingDiv = document.createElement('div');
    productRatingDiv.classList.add('product-rating');
    
    // logic to display rating icons
    for (let i = 0; i < Math.floor(product.rating); i++) {
        const ratingIcon = document.createElement('div');
        ratingIcon.textContent = '★'; 
        productRatingDiv.appendChild(ratingIcon);
    }
    for (let i = Math.floor(product.rating); i < 5; i++) {
        const emptyIcon = document.createElement('div');
        emptyIcon.classList.add('empty-icon');
        emptyIcon.textContent = '☆'; 
        productRatingDiv.appendChild(emptyIcon);
    }
    const ratingValue = document.createElement('div');
    ratingValue.classList.add('rating-value');
    ratingValue.textContent = product.rating; 
    productRatingDiv.appendChild(ratingValue);
    



    // Append all the parts to the product div
    productDiv.appendChild(productImageDiv);
    productDiv.appendChild(productNameDiv);
    productDiv.appendChild(productPriceDiv);
    productDiv.appendChild(productRatingDiv);

    // Append the product div to the products container
    popularProductsContainer.appendChild(productDiv);
});

featuredProducts.map(product => {
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
    const productName = document.createElement('h4');
    productName.textContent = product.name;
    productNameDiv.appendChild(productName);

    // Create and populate the price div
    const productPriceDiv = document.createElement('div');
    productPriceDiv.classList.add('product-price');
    productPriceDiv.textContent = `Price:  $${product.price}`;

    // Create and populate the rating div
    const productRatingDiv = document.createElement('div');
    productRatingDiv.classList.add('product-rating');
    
    // logic to display rating icons
    for (let i = 0; i < Math.floor(product.rating); i++) {
        const ratingIcon = document.createElement('div');
        ratingIcon.textContent = '★'; 
        productRatingDiv.appendChild(ratingIcon);
    }
    for (let i = Math.floor(product.rating); i < 5; i++) {
        const emptyIcon = document.createElement('div');
        emptyIcon.classList.add('empty-icon');
        emptyIcon.textContent = '☆'; 
        productRatingDiv.appendChild(emptyIcon);
    }
    const ratingValue = document.createElement('div');
    ratingValue.classList.add('rating-value');
    ratingValue.textContent = product.rating; 
    productRatingDiv.appendChild(ratingValue);
    



    // Append all the parts to the product div
    productDiv.appendChild(productImageDiv);
    productDiv.appendChild(productNameDiv);
    productDiv.appendChild(productPriceDiv);
    productDiv.appendChild(productRatingDiv);

    // Append the product div to the products container
    featuredProductsContainer.appendChild(productDiv);
});
