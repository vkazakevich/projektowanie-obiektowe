package models

import (
	"errors"

	"gorm.io/gorm"
)

type Payment struct {
	gorm.Model

	IsPaid bool `gorm:"not null"`
	Amount uint `gorm:"not null"`
}

func (p *Payment) BeforeCreate(tx *gorm.DB) (err error) {
	if p.Amount <= 0 {
		return errors.New("category name cannot be empty")
	}

	return nil
}
