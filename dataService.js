let catalog = [
    {
        _id: "1",
        title: "Air Jordan 1",
        price: 120,
        brand: "Nike",
        category: "Basketball shoes",
        image: "./images/jordans.png"
    },
    
    {
        _id: "2",
        title: "Nike LeBron 19",
        price: 130,
        brand: "Nike",
        category: "Basketball shoes",
        image: "./images/lebrons.png"
    },

    {
        _id: "3",
        title: "Nike Kyrie 8",
        price: 130,
        brand: "Nike",
        category: "Basketball shoes",
        image: "./images/kyrie.png"
    },

    {
        _id: "4",
        title: "Adidas Predator Edge",
        price: 120,
        brand: "Adidas",
        category: "Soccer shoes",
        image: "./images/adidas.png"
    }
];

class DataService{

    getCatalog(){
        // Call the server
        // Get the list of products and return it

        return catalog;
    }

}

export default DataService;