import axios from 'axios'

componentDidMount(){
    axios.get('https://jsonplaceholder.typicode.com/posts')
    .then(response => {
        this.setState({postList: response.data})
    })
    .catch(error => {
        console.log(error)
    })
}