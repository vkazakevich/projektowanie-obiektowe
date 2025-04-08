<?php

namespace App\Dto;

use Symfony\Component\Validator\Constraints as Assert;

class CustomerDto
{
    public function __construct(
        #[Assert\NotBlank]
        #[Assert\Length(max: 255)]
        public readonly string $firstName,

        #[Assert\NotBlank]
        #[Assert\Length(max: 255)]
        public readonly string $lastName,

        #[Assert\NotBlank]
        #[Assert\Email]
        public readonly string $email,
        
        
        #[Assert\Length(max: 255)]
        public readonly ?string $phone,
    ) {
    }
}