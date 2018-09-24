<template>
<div class="container">
  <h1>Poor Man's Twitter</h1>
  <div class="lds-ellipsis" v-if="this.loading">
    <div></div><div></div><div></div><div></div>
  </div>
<div class="form-group">
    <input type="name" class="form-control"
            placeholder="Put your name here" 
            v-model="name"
            @keyup.enter="addTweet"> 
    <input type="text" 
        placeholder="Say something" 
        v-model="text"
        @keyup.enter="addTweet"> 
  </div>
  <table id="twitts_table" class="table table-striped">
    <thead>
      <tr>
        <th v-for="column in columns" :key="column" @click="sortBy(column)">
            {{ column }}
        </th>
      </tr>
    </thead>

    <tbody>
      <!-- <tr v-for="twitt in twitts | orderBy sortKey reverse" :key="twitt.id"> -->
      <tr v-for="twitt in twitts " :key="twitt.id">
            <td class="lalign">{{twitt.name}}</td>
            <td>{{twitt.text}}</td>
            <td>{{twitt.twitt_date}}</td>
        </tr>
      
    </tbody>
  </table>

  
</div>


</template>

<script>
import JQuery from "jquery";
let $ = JQuery;

export default {
  name: "TwittsList",
  data() {
    return {
      loading: true,
      sortKey: "Name",
      reverse: false,
      text: "",
      name: "",
      csrf_token: "",
      columns: ["Name", "Text", "Date"],
      twitts: []
    };
  },
  methods: {
    processResult(data) {
      this.twitts = data;
      this.loading = false;
    },
    handleError(data) {
      this.loading = false;
      console.log(data)
    },
    makerequest(type) {
      const data =
        type == "POST"
          ? {
              csrfmiddlewaretoken: this.csrf_token,
              name: this.name,
              text: this.text
            }
          : "";
      $.ajax({
        url: "http://localhost:8000/",
        type: type,
        dataType: "json",
        headers: {'X-CSRFToken': this.csrf_token},
        data: data,
        cache: false,
        success: this.processResult,
        error: this.handleError,
        async: true
      });
    },
    addTweet() {
      if (this.name.trim().length == 0 || this.text.trim().length == 0) {
        return;
      }
      this.loading = true;
      this.makerequest("POST");
      this.name = "";
      this.text = "";
    },
    getToken() {
      $.ajax({
        url: 'http://localhost:8000/get-token/',
        type: 'GET',
        dataType: 'json',
        success: (data) => {
          this.csrf_token = data.token
        }
      });
    },
    sortBy(sortKey) {
      if(sortKey != this.sortKey) {
        this.sortKey = sortKey
      } else {
        this.reverse = !this.reverse 
      }
      if(sortKey === 'Name') {
        this.twitts = this.sortedTweetsByName
      } else {
        this.twitts = this.sortedTweetsByDate
      }
    }
  },
  computed: {
    sortedTweetsByName() {
      const twitts = this.twitts.sort( (a, b) => {
        if (a.name < b.name)
          return -1;
        if (a.name > b.name)
          return 1;
        return 0;
      })
      return this.reverse ? twitts.reverse() : twitts
      
    },
    sortedTweetsByDate() {
      const twitts = this.twitts.sort( (a, b) => {
        const aDate = new Date(a.twitt_date)
        const bDate = new Date(b.twitt_date)
        if (aDate < bDate)
          return -1;
        if (aDate > bDate)
          return 1;
        return 0;
      })
      return this.reverse ? twitts.reverse() : twitts
    }
  },
  created() {
    this.makerequest("GET");
    this.getToken();
  }
};
</script>

<style>

#twitts_table {
    font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

#twitts_table td, #twitts_table th {
    border: 1px solid #ddd;
    padding: 8px;
}

#twitts_table tr:nth-child(even){background-color: #f2f2f2;}

#twitts_table tr:hover {background-color: #ddd;}

#twitts_table th {
    padding-top: 12px;
    padding-bottom: 12px;
    text-align: left;
    background-color: #4CAF50;
    color: white;
}


.lds-ellipsis {
  display: block;
  position: relative;
  width: 64px;
  height: 64px;
  margin: auto;
  margin-bottom: 16px;
}
.lds-ellipsis div {
  position: absolute;
  top: 27px;
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: rgb(126, 67, 8);
  animation-timing-function: cubic-bezier(0, 1, 1, 0);
}
.lds-ellipsis div:nth-child(1) {
  left: 6px;
  animation: lds-ellipsis1 0.6s infinite;
}
.lds-ellipsis div:nth-child(2) {
  left: 6px;
  animation: lds-ellipsis2 0.6s infinite;
}
.lds-ellipsis div:nth-child(3) {
  left: 26px;
  animation: lds-ellipsis2 0.6s infinite;
}
.lds-ellipsis div:nth-child(4) {
  left: 45px;
  animation: lds-ellipsis3 0.6s infinite;
}
@keyframes lds-ellipsis1 {
  0% {
    transform: scale(0);
  }
  100% {
    transform: scale(1);
  }
}
@keyframes lds-ellipsis3 {
  0% {
    transform: scale(1);
  }
  100% {
    transform: scale(0);
  }
}
@keyframes lds-ellipsis2 {
  0% {
    transform: translate(0, 0);
  }
  100% {
    transform: translate(19px, 0);
  }
}

</style>



