package com.misiontic.cart_ms.models;
import org.springframework.data.annotation.Id;
import java.util.Date;
public class Cart {
    @Id
    private String id; /* La idea es que cada artículo agregado al carrito crea un registro */
    private String username;
    private String name;  /* Nombre del producto */
    private Integer value;  /* Precio del producto */
    private Integer amount;  /* Cantidad de unidades del producto */

    public Cart(String id, String username, String name, Integer value, Integer amount) {
        this.id = id;
        this.username = username;
        this.name = name;
        this.value = value;
        this.amount = amount;
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

    public Integer getValue() {
        return value;
    }

    public void setValue(Integer value) {
        this.value = value;
    }

    public Integer getAmount() {
        return amount;
    }

    public void setAmount(Integer amount) {
        this.amount = amount;
    }
}