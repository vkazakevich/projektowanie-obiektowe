package models

import (
	"errors"
	"strings"

	"gorm.io/gorm"
)

type Category struct {
	ID       uint      `gorm:"primarykey"`
	Name     string    `gorm:"not null" json:"name"`
	Products []Product `json:"products,omitempty"`
}

func (c *Category) BeforeCreate(tx *gorm.DB) (err error) {
	if strings.TrimSpace(c.Name) == "" {
		return errors.New("category name cannot be empty")
	}
	return nil
}

func WithProducts(db *gorm.DB) *gorm.DB {
	return db.Preload("Products")
}

func HasProducts(db *gorm.DB) *gorm.DB {
	return db.Joins("JOIN products ON products.category_id = categories.id").
		Group("categories.id").
		Having("COUNT(products.id) > ?", 0)
}
