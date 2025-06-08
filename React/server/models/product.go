package models

import (
	"errors"
	"strings"

	"gorm.io/gorm"
)

type Product struct {
	gorm.Model
	Name       string   `gorm:"not null" json:"name"`
	Price      uint     `json:"price"`
	Quantity   uint     `json:"quantity"`
	CategoryID uint     `json:"category_id"`
	Category   Category `json:"-"`
}

func (c *Product) BeforeCreate(tx *gorm.DB) (err error) {
	if strings.TrimSpace(c.Name) == "" {
		return errors.New("product name cannot be empty")
	}

	if c.Price <= 0 {
		return errors.New("product price cannot be zero")
	}

	if c.Quantity <= 0 {
		return errors.New("product quantity cannot be zero")
	}

	return nil
}
