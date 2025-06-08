package models

import (
	"errors"
	"strings"

	"gorm.io/gorm"
)

type Customer struct {
	gorm.Model
	FirstName string `gorm:"not null"`
	LastName  string `gorm:"not null"`
	Email     string `gorm:"not null"`
	CartItems []Cart `gorm:"foreignKey:CustomerID"`
}

func (c *Customer) BeforeCreate(tx *gorm.DB) (err error) {
	if strings.TrimSpace(c.FirstName) == "" {
		return errors.New("customer last name cannot be empty")
	}

	if strings.TrimSpace(c.LastName) == "" {
		return errors.New("customer first name cannot be empty")
	}

	if strings.TrimSpace(c.Email) == "" {
		return errors.New("customer email cannot be empty")
	}
	return nil
}
