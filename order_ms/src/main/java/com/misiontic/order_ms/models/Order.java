package com.misiontic.order_ms.models;

import org.springframework.data.annotation.Id;

import java.util.List;

public class Order {
    @Id
    private String id;
    private String username;
    private String name;
    private Integer quantity;
    private Integer total;

    public Order(String id, String username, String name, Integer quantity, Integer total){
        this.id = id;
        this.username = username;
        this.name = name;
        this.quantity = quantity;
        this.total = total;
    }

    public String getId() {
        return id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getQuantity() {
        return quantity;
    }

    public void setQuantity(Integer quantity) {
        this.quantity = quantity;
    }

    public Integer getTotal() {
        return total;
    }

    public void setTotal(Integer total) {
        this.total = total;
    }

}   
