package com.misiontic.cart_ms.models;

import org.springframework.data.annotation.Id;

import java.util.List;

public class Order {
    @Id
    private String id;
    private List<Cart> content;
    private Integer total;
}   
