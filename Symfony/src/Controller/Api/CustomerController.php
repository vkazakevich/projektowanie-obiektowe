<?php

namespace App\Controller\Api;

use App\Dto\CustomerDto;
use App\Entity\Customer;
use App\Repository\CustomerRepository;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\HttpKernel\Attribute\MapRequestPayload;

#[Route('/api/customers')]
final class CustomerController extends AbstractController
{
    #[Route(name: 'api_customer', methods: ['GET'])]
    public function index(CustomerRepository $customerRepository): JsonResponse
    {
        return $this->json($customerRepository->findAll());
    }

    #[Route(name: 'api_customer_create', methods: ['POST'])]
    public function create(
        #[MapRequestPayload] CustomerDto $customerDto,
        CustomerRepository $customerRepository
    ): JsonResponse {
        $customer = new Customer();

        $customer->setFirstName($customerDto->firstName);
        $customer->setLastName($customerDto->lastName);
        $customer->setEmail($customerDto->email);
        $customer->setPhone($customerDto->phone);

        $customerRepository->save($customer, true);

        return $this->json($customer, Response::HTTP_CREATED);
    }

    #[Route('/{id}', name: 'api_customer_show', methods: ['GET'])]
    public function show(Customer $customer): JsonResponse
    {
        return $this->json($customer);
    }

    #[Route('/{id}', name: 'api_customer_update', methods: ['PUT'])]
    public function update(
        #[MapRequestPayload] CustomerDto $customerDto,
        Customer $customer,
        CustomerRepository $customerRepository
    ): JsonResponse {
        $customer->setFirstName($customerDto->firstName);
        $customer->setLastName($customerDto->lastName);
        $customer->setEmail($customerDto->email);
        $customer->setPhone($customerDto->phone);
        
        $customerRepository->save($customer, true);

        return $this->json($customer);
    }

    #[Route('/{id}', name: 'api_customer_delete', methods: ['DELETE'])]
    public function delete(Customer $customer, CustomerRepository $customerRepository): JsonResponse
    {
        $customerRepository->remove($customer, true);

        return $this->json('', Response::HTTP_NO_CONTENT);
    }
}
