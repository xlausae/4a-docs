package com.misiontic.order_ms.models;

import org.springframework.data.annotation.Id;
import java.util.Date;

public class Order {
    @Id
    private String id;
    private String username;
    private String name;    /* Nombre del producto */
    private Integer quantity;
    private Integer total;
    private Date date;

    public Order(String id, String username, String name, Integer quantity, Integer total, Date date) {
        this.id = id;
        this.username = username;
        this.name = name;
        this.quantity = quantity;
        this.total = total;
        this.date = date;
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

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }
}
