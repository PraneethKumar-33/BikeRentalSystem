package com.bikerental.models;

import jakarta.persistence.*;

@Entity
@Table(name = "bikes")
public class Bike {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String modelName;
    private String category; // e.g., "Mountain", "City"
    private double dailyRate;
    private boolean available;

    public Bike() {}

    public Bike(String modelName, String category, double dailyRate, boolean available) {
        this.modelName = modelName;
        this.category = category;
        this.dailyRate = dailyRate;
        this.available = available;
    }

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getModelName() { return modelName; }
    public void setModelName(String modelName) { this.modelName = modelName; }
    public String getCategory() { return category; }
    public void setCategory(String category) { this.category = category; }
    public double getDailyRate() { return dailyRate; }
    public void setDailyRate(double dailyRate) { this.dailyRate = dailyRate; }
    public boolean isAvailable() { return available; }
    public void setAvailable(boolean available) { this.available = available; }
}
